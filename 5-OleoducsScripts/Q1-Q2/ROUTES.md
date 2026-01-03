# Routes

## LOAD-BALANCER

### Status

- **GET** `http://MY_DOMAIN/`  
  Confirms that the server is running.

### Partie DevOps

- **GET** `http://MY_DOMAIN/leader`  
  Retrieves the domain of the REDIS leader.
- **POST** `http://MY_DOMAIN/leader`  
  Triggers the election of a new leader.
- **ANY** `http://MY_DOMAIN/api/*ANY_WILDCARD*`  
  Forwards the request to `http://CONSULT_DB_SLAVE/*ANY_WILDCARD*`.

---

## CONSULT_DB_SLAVE

### Status

- **GET** `http://MY_DOMAIN/`  
  Confirms that the server is running.
- **GET** `http://MY_DOMAIN/health`  
  Confirms that REDIS is running.

### Partie DevOps

- **POST** `http://MY_DOMAIN/elect-new`  
  **BODY:** `{ domain: string?, port: number? }`  
  Specifies which REDIS instance to use.

### Fonctionnalité Redis/Store

- **GET** `http://MY_DOMAIN/get-value/:key`  
  Reads a value associated with the given key.
- **GET** `http://MY_DOMAIN/keys`  
  Retrieves all keys stored in REDIS.
- **POST** `http://MY_DOMAIN/set-value`  
  **BODY:** `{ key, value }`  
  Inserts an object into the store.
