<template>
    <div v-for="product in ValueObjetos" class="information">
        <h1>Información del libro</h1>
        <h2>Nombre: <span>{{name_prod}}</span></h2>
        <h2>precio: <span>{{price}} COP </span></h2>
        <h2>autor: <span>{{author}}</span></h2>
    </div>
</template>

<script>
import axios from 'axios';
import { objectExpression } from "@babel/types";

export default {
    name: "Products",
    data: function () {
        return {
            name_prod: "",
            author: "",
            price: 0,
            loaded: true,
        }
    },
    methods: {
        getData: function () {

            axios.get(`http://127.0.0.1:8000/products/`)
                .then((result) => {
                    var productsArr = [];

                    Object.entries(result).forEach(arr => {
                        const key = arr[0]
                        const value = arr[1]
                        productsArr = Object.values(value)

                        const datos = productsArr.map((item) => {
                            return item
                        });
                        const obtenerData = datos.forEach(item => {
                            return console.log("hola", item)
                        });
                        // console.log(obtenerData)
                        // console.log(datos)
                        // const ValueObjetos = Object.values(productsArr);
                        // console.log(ValueObjetos[0])
                    })

                    //alert(productsArr)
                    this.loaded = true;
                })
                .catch((e) => {
                    alert(e)
                });
        },

    },
    created: async function () {
        this.getData();
    },
}
</script>
<style>
.information {
    margin: 0;
    padding: 0%;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

information h1 {
    font-size: 60px;
    color: #0f1316;
}

.information h2 {
    font-size: 40px;
    color: #283747;
}

.information span {
    color: crimson;
    font-weight: bold;
}
</style>