<template>
  <v-container>
    <v-btn @click="fetch" class="pink" :disabled="Loading" :loading="Loading">Uppdatera</v-btn>
    <v-data-table :loaing="Loading" :headers="headers" :items="info" class="elevation-1"></v-data-table>
    <v-snackbar v-model="snackbar">
      {{ snackbar_text }}
      <v-btn :color="snackbar_type" text @click="snackbar = false">Close</v-btn>
    </v-snackbar>
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
      Loading: false,
      snackbar: false,
      snackbar_text: "",
      snackbar_type: "success",
      headers: [
        {
          text: "Skola",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "Pengar insamlat (kr)", value: "cash" }
        // { text: "Ansvarig lärare", value: "ansv" },
        // { text: "Senaste Bidrag", value: "bid" },
        // { text: "Senaste Uppdatering", value: "tid" }
      ],
      info: [
        {
          name: "Laddar",
          cash: "Laddar mer",
          ansv: "Laddar ännu mer",
          tid: "kolla din uppkoppling"
        }
      ]
    };
  },
  methods: {
    fetch() {
      let self = this;
      let out = "";

      self.info = []

      self.Loading = true

      //Ändra denna URL så funkar för din API eller enhet
      axios
        .get(
          "https://bossan.musikhjalpen.se/insamlingar/abbe-abb-industrigymnasium"
        )
        .then(function(response) {
          let re = /<h1 class="font-thick">.+kr/i;
          out = response.data.match(re)[0];
          let Tal = out.replace('<h1 class="font-thick">', "");
          out = Tal.replace(" ", "");

          self.info.push({
            name: "ABB",
            cash: Tal
          });

          // self.snackbar_text = parseInt(out);
          // self.snackbar = true;
        })
        .catch(function(error) {
          /* eslint-disable */
          console.log(error);
        });

      axios
        .get(
          "https://bossan.musikhjalpen.se/insamlingar/rudbeckianska-gymnasiet-orginalet-sedan-1623"
        )
        .then(function(response) {
          let re = /<h1 class="font-thick">.+kr/i;
          out = response.data.match(re)[0];
          let Tal = out.replace('<h1 class="font-thick">', "");
          out = Tal.replace(" ", "");

          self.info.push({
            name: "Rudbeck",
            cash: Tal
          });

          // self.snackbar_text = parseInt(out);
          // self.snackbar = true;
        })
        .catch(function(error) {
          /* eslint-disable */
          console.log(error);
        });
      axios
        .get(
          "https://bossan.musikhjalpen.se/insamlingar/grillska-gymnasiet-vasteras-for-musikhjalpen-2019"
        )
        .then(function(response) {
          let re = /<h1 class="font-thick">.+kr/i;
          out = response.data.match(re)[0];
          let Tal = out.replace('<h1 class="font-thick">', "");
          out = Tal.replace(" ", "");

          self.info.push({
            name: "Grillska",
            cash: Tal
          });

          // self.snackbar_text = parseInt(out);
          // self.snackbar = true;
        })
        .catch(function(error) {
          /* eslint-disable */
          console.log(error);
        });
      axios
        .get(
          "https://bossan.musikhjalpen.se/insamlingar/abbe-abb-industrigymnasium"
        )
        .then(function(response) {
          let re = /<h1 class="font-thick">.+kr/i;
          out = response.data.match(re)[0];
          let Tal = out.replace('<h1 class="font-thick">', "");
          out = Tal.replace(" ", "");

          self.info.push({
            name: "Wjikmanska",
            cash: "har ingen än?"
          });
          self.Loading = false

          // self.snackbar_text = parseInt(out);
          // self.snackbar = true;
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
