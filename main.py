import json
from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException


app = FastAPI(
    title='FastAPI prototype for the partners\' location\'s project',
    description='This API is a small prototype to be used for the partner\'s'
                'location project',
    version='1.0.0'
)


@app.get('/')
def get_index():
    """Root's endpoint
    """
    return { 'name': 'Partners\' location\'s FastAPI prototype' }


@app.get('/partners')
def get_partners(hint: str = ''):
    """Get all partners
    """
    with open('./data/partners.json', 'r') as json_file:
        partners = json.load(json_file)

    if not hint:
        return partners
    
    return [partner for partner in partners if hint in partner['name']]


@app.get('/partners/{partner_id}')
def get_partner(partner_id: int):
    """Get a partner by its index
    """
    with open('./data/partners.json', 'r') as json_file:
        partners = json.load(json_file)

    if partner_id >= len(partners):
        raise HTTPException(status_code=404, detail="Item not found")

    return partners[partner_id]
