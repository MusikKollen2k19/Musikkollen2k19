<template>
    <v-container>
        <v-btn @click="fetch" class="pink">Uppdatera</v-btn>
  <v-data-table 
    :headers="headers"
    :items="desserts"
    class="elevation-1"
  ></v-data-table>
   </v-container>
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
          { text: 'Senaste Bidrag', value: 'bid' },
          { text: 'Senaste Uppdatering', value: 'tid' },
        ],
        desserts: [
          {
            name: 'Grillska',
            cash: 50,
            ansv: "Bruh Momento",
            bid: 0.4,
            tid: "19:20:00:70",
          },
          {
            name: 'Rudbeck',
            cash: 1,
            ansv: "Big Ounce, professional gangstar",
            bid: 780,
            tid: "19:20:00:70",
          },
          {
            name: "Wijkmanska",
            cash: 50.5,
            ansv: "JoJo",
            bid: 13,
            tid: "19:20:00:70",
          },
          {
            name: "es",
            cash: 500000,
            ansv: "ertg",
            bid: 69,
            tid: "19:20:00:70",
          },
        ],
      }
    },
    methods: {
        fetch(){
          let self = this;
          
     //Ändra denna URL så funkar för din API eller enhet
     axios.get("https://km1wzv5ri1.execute-api.us-east-1.amazonaws.com/v1")
  .then(function (response) {
    
    for (let i = 0; i < response.data.length; i++) {
      if(response.data[i].Skola == "Grillska") {
          self.desserts[0].name=response.data[i].Skola;
          self.desserts[0].cash=response.data[i].CurrentAmount;
          self.desserts[0].ansv=response.data[i].Ansvarig;
          self.desserts[0].tid=response.data[i].LastUpdate[response.data[i].LastUpdate.length -1];
          self.desserts[0].bid=response.data[i].LastAmount[response.data[i].LastAmount.length -1];
      } else if(response.data[i].Skola == "Rusbeck") {
          self.desserts[1].name=response.data[i].Skola;
          self.desserts[1].cash=response.data[i].CurrentAmount;
          self.desserts[1].ansv=response.data[i].Ansvarig;
          self.desserts[1].tid=response.data[i].LastUpdate[response.data[i].LastUpdate.length -1];
          self.desserts[1].bid=response.data[i].LastAmount[response.data[i].LastAmount.length -1];
      } else if(response.data[i].Skola == "Wijkmanska") {
          self.desserts[2].name=response.data[i].Skola;
          self.desserts[2].cash=response.data[i].CurrentAmount;
          self.desserts[2].ansv=response.data[i].Ansvarig;
          self.desserts[2].tid=response.data[i].LastUpdate[response.data[i].LastUpdate.length -1];
          self.desserts[2].bid=response.data[i].LastAmount[response.data[i].LastAmount.length -1];
      } else if(response.data[i].Skola == "ABB") {
          self.desserts[3].name=response.data[i].Skola;
          self.desserts[3].cash=response.data[i].CurrentAmount;
          self.desserts[3].ansv=response.data[i].Ansvarig;
          self.desserts[3].tid=response.data[i].LastUpdate[response.data[i].LastUpdate.length -1];
          self.desserts[3].bid=response.data[i].LastAmount[response.data[i].LastAmount.length -1];
      }
    }
    // self.desserts[3].name=response.data[0].Skola;
    // self.desserts[3].cash=response.data[0].CurrentAmount;
    // self.desserts[3].ansv=response.data[0].Ansvarig;
    //     self.desserts[2].name=response.data[0].Skola;
    // self.desserts[2].cash=response.data[0].CurrentAmount;
    // self.desserts[2].ansv=response.data[0].Ansvarig;
    //     self.desserts[1].name=response.data[0].Skola;
    // self.desserts[1].cash=response.data[0].CurrentAmount;
    // self.desserts[1].ansv=response.data[0].Ansvarig;
    //     self.desserts[0].name=response.data[0].Skola;
    // self.desserts[0].cash=response.data[0].CurrentAmount;
    // self.desserts[0].ansv=response.data[0].Ansvarig;
    })
    .catch(function (error) {
    
       /* eslint-disable */
       console.log(error);
  });
    }
    },
    links: [{
      route: "/login",
    }],
  }
</script>
<style>
  #Cooltext {
    color: black;
    text-decoration: underline;
  }
</style>