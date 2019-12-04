<template>
  <v-container>
    <v-btn @click="fetch" class="pink">Uppdatera</v-btn>
    <v-data-table :headers="headers" :items="info" class="elevation-1"></v-data-table>
  </v-container>
</template>
 
<script>
const axios = require("axios");
export default {
  created() {
    this.fetch();
  },
  name: "Chart",
  data() {
    return {
      Messagedata: "dddffffjjjjjdd",
      Ansvar: "ty",
      Siffra: 69,
      headers: [
        {
          text: "Skola",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "Pengar insamlat (kr)", value: "cash" },
        { text: "Ansvarig lärare", value: "ansv" }
      ],
      info: [
        {
          name: "Laddar",
          cash: "Laddar mer",
          ansv: "Laddar ännu mer"
        }
      ]
    };
  },
  methods: {
    fetch() {
      let self = this;

      //Ändra denna URL så funkar för din API eller enhet
      axios
        .get("https://km1wzv5ri1.execute-api.us-east-1.amazonaws.com/v1")
        .then(function(response) {
          // console.log(response.data);
          self.info = [];

          response.data.forEach(element => {
            // console.log(element);
            self.info.push({name: element.Skola, cash: element.CurrentAmount, ansv: element.Ansvarig})
          });

          /* eslint-disable */
          // self.desserts[3].name = response.data[0].Skola;
          // self.desserts[3].cash = response.data[0].CurrentAmount;
          // self.desserts[3].ansv = response.data[0].Ansvarig;
          // self.desserts[2].name = response.data[0].Skola;
          // self.desserts[2].cash = response.data[0].CurrentAmount;
          // self.desserts[2].ansv = response.data[0].Ansvarig;
          // self.desserts[1].name = response.data[0].Skola;
          // self.desserts[1].cash = response.data[0].CurrentAmount;
          // self.desserts[1].ansv = response.data[0].Ansvarig;
          // self.desserts[0].name = response.data[0].Skola;
          // self.desserts[0].cash = response.data[0].CurrentAmount;
          // self.desserts[0].ansv = response.data[0].Ansvarig;
        })
        .catch(function(error) {
          /* eslint-disable */
          console.log(error);
        });
    }
  },
  links: [
    {
      route: "/login"
    }
  ]
};
</script>
<style>
#Cooltext {
  color: black;
  text-decoration: underline;
}
</style>
