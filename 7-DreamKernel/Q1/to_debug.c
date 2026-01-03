#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <signal.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <time.h>
#include <stdint.h>

// --- Globals ---
int bufferSize;

sem_t producerTokens; // free slots for producers
sem_t consumerTokens; // items available for consumers
sem_t accessMutex;    // mutex

char *digitBuffer;

volatile sig_atomic_t endFlag = 0;
int ip = 0;
int ic = 0;

int totalGenerated = 0;
int totalConsumed = 0;

// --- Signal handler ---
static void alarm_set(int signum)
{
    (void)signum;
    endFlag = 1;
}

// --- Threads ---
void *producer(void *pid)
{
    long id = (long)pid;
    int producedCount = 0;

    for (;;)
    {
        sem_wait(&accessMutex);
        sem_wait(&producerTokens);

        if (endFlag)
        {
            sem_post(&accessMutex);
            sem_post(&producerTokens);
            break;
        }

        char val = '0' + rand() % 10;
        digitBuffer[ip] = val;
        printf("[Prod %ld] produit '%c' à pos %d\n", id, val, ip);

        producedCount++;
        totalGenerated++;
        ip = (ip + 1) % bufferSize;

        sem_post(&accessMutex);
        sem_post(&consumerTokens);
    }

    printf("Producteur %ld a produit %d lettres\n", id, producedCount);
    return NULL;
}

void *consumer(void *cid)
{
    long id = (long)cid;
    int consumedCount = 0;

    for (;;)
    {
        sem_wait(&consumerTokens);
        sem_wait(&accessMutex);

        int consumedValue = digitBuffer[ic];
        printf("[Cons %ld] consomme '%c' à pos %d\n", id, (consumedValue ? consumedValue : '-'), ic);

        ic = (ic + 1) % bufferSize;
        sem_post(&accessMutex);
        sem_post(&producerTokens);

        if (consumedValue == 0)
        {
            break;
        }

        consumedCount++;
        totalConsumed++;
    }

    printf("Consommateur %ld a consommé %d lettres\n", id, consumedCount);
    return NULL;
}

// --- main ---
int main(int argc, char *argv[])
{
    if (argc < 4)
    {
        fprintf(stderr, "Usage: %s <nbProducteurs> <nbConsommateurs> <tailleTampon>\n", argv[0]);
        return 1;
    }

    int numProducers = atoi(argv[1]);
    int numConsumers = atoi(argv[2]);
    bufferSize = atoi(argv[3]);

    srand((unsigned)time(NULL));

    digitBuffer = calloc((size_t)bufferSize, sizeof(char));
    pthread_t *producers = malloc((size_t)numProducers * sizeof(pthread_t));
    pthread_t *consumers = malloc((size_t)numConsumers * sizeof(pthread_t));

    sem_init(&producerTokens, 0, (unsigned)bufferSize);
    sem_init(&consumerTokens, 0, 0);
    sem_init(&accessMutex, 0, 1);

    signal(SIGALRM, alarm_set);

    for (long i = 0; i < numProducers; ++i)
    {
        pthread_create(&producers[i], NULL, producer, (void *)i);
    }
    for (long i = 0; i < numConsumers; ++i)
    {
        pthread_create(&consumers[i], NULL, consumer, (void *)i);
    }

    alarm(5); // Adjust to see race conditions between producers and consumers

    while (!endFlag)
    {
        sleep(5000);
    }
    for (int i = 0; i < numProducers; ++i)
    {
        sem_post(&producerTokens);
    }
    for (int i = 0; i < numProducers; ++i)
    {
        pthread_join(producers[i], NULL);
    }

    for (int i = 0; i < numConsumers; ++i)
    {
        sem_wait(&accessMutex);
        sem_wait(&producerTokens);
        digitBuffer[ip] = 0;
        printf("[Main] poison pill à pos %d\n", ip);
        ip = (ip + 1) % bufferSize;
        sem_post(&accessMutex);
        sem_post(&consumerTokens);
    }

    for (int i = 0; i < numConsumers; ++i)
    {
        pthread_join(consumers[i], NULL);
    }

    printf("Total Consommés: %d\n", totalConsumed);
    printf("Total Générés:  %d\n", totalGenerated);

    sem_destroy(&producerTokens);
    sem_destroy(&consumerTokens);
    sem_destroy(&accessMutex);
    free(digitBuffer);
    free(producers);
    free(consumers);

    return 0;
}
