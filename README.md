# Interaktivni sadržaj - igra Memory

## Source code
Source code interaktivnog sadržaja, web igre Memory

## Link stranice
https://samsung.kada.works/


## API Reference

#### Get wins
Vraća trenutni ukupni broj pobjeda.

```http
GET /api/wins
```

#### Response

```json
{
  "value": 42
}
```

#### Increment wins
Povećava broj pobjeda za 1 i čuva novu vrijednost.

```http
POST /api/hit
```
