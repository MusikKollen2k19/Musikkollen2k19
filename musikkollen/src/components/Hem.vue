<template>
    <v-container>
        <v-btn @click="fetch">Uppdatera</v-btn>
    </v-container>
</template>
<script>
const axios = require("axios");
export default {
    name: "Hem",

    methods: {
        async fetch() {
            const {data} = await axios.get("https://km1wzv5ri1.execute-api.us-east-1.amazonaws.com/v1"); //URLen för databasen, skickas en GET-request till URLen
            console.log(data);
        }
    }
}
</script>