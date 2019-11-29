<template>
  <v-data-table 
    :headers="headers"
    :items="desserts"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
const axios = require("axios");
  export default {
    created(){
  this.fetch();
},
    name: "Chart",
    data () {
      return {
        headers: [
          {
            text: "Skola",
            align: 'left',
            sortable: false,
            value: 'name',
          },
          { text: 'Pengar insamlat (kr)', value: 'cash' },
          { text: 'Ansvarig lärare', value: 'ansv' },
        ],
        desserts: [
          {
            name: 'Grillska',
            cash: 50,
            ansv: "Bruh Momento",
          },
          {
            name: 'Rudbeck',
            cash: 1,
            ansv: "Big Ounce, professional gangstar",
          },
          {
            name: "Wijkmanska",
            cash: 50.5,
            ansv: "JoJo",
          },
          {
            name: 'ABB',
            cash: 500000,
            ansv: "William Sonnerklev",
          },
        ],
      }
    },
    methods: {
        async fetch() {
        let self=this;
        const {data} = await axios.get("https://ovtay1b689.execute-api.us-east-1.amazonaws.com/Temp/device/data?name=Joels_Enhet"); //URLen för databasen, skickas en GET-request till URLen
        self.Messagedata=data;
        /* eslint-disable */
        console.log(data);
        }
    }
    }
</script>