from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Définir la structure des données
class Item(BaseModel):
    text: str
    is_done: bool = False

# Créer l'application FastAPI
app = FastAPI()

# Liste des items (base de données simulée)
items = [{"text": "apple", "is_done": False}, {"text": "banana", "is_done": False}]

# Route pour obtenir tous les items
@app.get("/items")
def list_items():
    return {"message": "Liste des items", "items": items}

# Route pour obtenir un item par son ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(items):
        return {"message": f"Item trouvé avec l'ID {item_id}", "item": items[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# Route pour ajouter un item
@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return {"message": "Item ajouté avec succès", "item": item}

# Route pour mettre à jour un item par son ID
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id < len(items):
        old_item = items[item_id]
        items[item_id] = item.dict()  # Remplace l'item avec l'ID donné
        return {
            "message": f"Item avec l'ID {item_id} mis à jour",
            "old_item": old_item,
            "new_item": item.dict()
        }
    else:
        raise HTTPException(status_code=404, detail="Item not found")
