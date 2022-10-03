<template>
    <div>
        <ul>
            <li v-for="product in productsArr" id="information" class=" informacion">
                <strong>Información del libro</strong><br/>
                <strong> Nombre: {{product.name_prod}}</strong><br/>
                <strong>precio: {{product.price}} COP </strong><br/>
                <strong>autor: {{product.author}}</strong><br/>
                <button> Comprar</button>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';
import { objectExpression } from "@babel/types";
   
export default {
    name: "GetBook",

    el: '#information',
    
    data: function(){
        return {
            productsArr: [
        {
            "product": 1,
            "name_prod": "1001 años",
            "author": "julian",
            "editorial": "dos",
            "category": "uno",
            "type_prod": "libro",
            "num_page": 354,
            "isbn": "1",
            "state": "good",
            "rank": "10",
            "format_prod": "pdf",
            "presentation": "libro",
            "image": "dkd",
            "price": "200.000",
            "visits": 4,
            "description": "libro prueba",
            "name_cat": "jdjf",
            "subcategory": "fmmg",
            "inventory_id": 1,
            "sale_id": 1,
            "user_id": 1
        },
        {
            "product": 2,
            "name_prod": "la maria",
            "author": "jorge",
            "editorial": "planeta",
            "category": "uno",
            "type_prod": "libro",
            "num_page": 354,
            "isbn": "1",
            "state": "good",
            "rank": "10",
            "format_prod": "pdf",
            "presentation": "libro",
            "image": "dkd",
            "price": "200.000",
            "visits": 4,
            "description": "libro prueba",
            "name_cat": "jdjf",
            "subcategory": "fmmg",
            "inventory_id": 1,
            "sale_id": 1,
            "user_id": 1
        },
        {
            "product": 3,
            "name_prod": "alquimista",
            "author": "coelho",
            "editorial": "planeta",
            "category": "uno",
            "type_prod": "libro",
            "num_page": 354,
            "isbn": "1",
            "state": "good",
            "rank": "10",
            "format_prod": "pdf",
            "presentation": "libro",
            "image": "dkd",
            "price": "200.000",
            "visits": 4,
            "description": "libro prueba",
            "name_cat": "jdjf",
            "subcategory": "fmmg",
            "inventory_id": 1,
            "sale_id": 1,
            "user_id": 1
        }
    ]
        }},

    methods: {
        getData:  function () {
                        
            axios.get(`http://127.0.0.1:8000/products/`)
                .then((result) => {                    
                    var n = Object.values(result)
                    var m = n [0]
                    var c = Object.entries(m)
                    var b = c [0]
                    var productsArr = b [1]
                   
                    console.log(productsArr)
                    this.loaded = true;
                    
                })
                return productsArr
                .catch((e) => {
                    alert (e)
                });
                
        },
            
    },
 created: async function(){
    this.getData();
 },
}
</script>
<style>
li{
    border: 2px
} 

 .information{
    margin: 0;
    padding: 0%;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
 }
 information h1{
    font-size: 60px;
    color: #0f1316;
    }
    .information h2{
    font-size: 40px;
    color: #283747;
    }
    .information span{
    color: crimson;
    font-weight: bold;
    }
   </style>