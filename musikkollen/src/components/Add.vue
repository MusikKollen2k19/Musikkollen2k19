<template>
  <v-app id="background" fixed>
    <v-container bg fill-height grid-list-md text-xs-center>
      <v-row>
        <v-flex xs4 offset-4>
          <v-card max-width="450" elevation="20" justify-center align-center class-mx-auto id="a6" > 
            <h1 id="a3">Lägg till summa</h1>
            <div class="flex-grow-1"></div>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }"></template>
            </v-tooltip>
            <v-tooltip right>
              <template v-slot:activator="{ on }"></template>
            </v-tooltip>

            <v-card-text>
              <v-form v-model="valid">
                <v-text-field
                  label="Användarnamn"
                  name="Användarnamn"
                  type="text"
                  v-model="login"
                  :rules="loginRules"
                  required
                ></v-text-field>

                <v-text-field
                  label="Lösenord"
                  name="Lösenord"
                  type="password"
                  v-model="password"
                  :rules="passwordRules"
                  required
                ></v-text-field>

                <v-text-field
                  label="Antal kronor"
                  name="SEK"
                  type="number"
                  v-model="sek"
                  :rules="sekRules"
                  required
                ></v-text-field>
              </v-form>
              <v-card-actions>
                <v-btn
                  :disabled="!valid"
                  id="a5"
                  xs12
                  color="primary"
                  block
                  tile
                  @click="submit"
                >Lägg till</v-btn>
              </v-card-actions>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
/* eslint-disable */
import router from "../router";
// eslint-disable-next-line
const sha256 = require("js-sha256");
// eslint-disable-next-line
const axios = require("axios");
export default {
  props: {
    source: String
  },
  data: () => ({
    drawer: 0,
    sek: "",
    login: "",
    valid: true,
    loginRules: [v => (v && v.length >= 3) || "Användarnamn är för kort!"],
    password: "",
    passwordRules: [
      v => !!v || "Ett lösenord krävs!",
      v => (v && v.length >= 8) || "Lösenordet är för kort!"
    ],
    sekRules: [
      v => !!v || "Ett nummer krävs!",
      v => (v && typeof(v) != 'number') || "Inte ett Nummer!"
    ]
  }),
  methods: {
    submit() {
      // ToDo user gets an id on reg that gets stored in the db next to pass.
      // user needs an id to remove their devices
      // lambda checks in database if user and pass hash matches and sends back an id
      // vuex keeps the id
      // eslint-disable-next-line
      console.log(this.$refs.form);

      // if (this.$refs.form.validate()) {

      var log = this.login;

      let body = { user: this.login, pass: sha256(this.password), Amount: parseInt(this.sek)};
      let stringbody = JSON.stringify(body);
      console.log(stringbody)
      axios.post(
          "https://km1wzv5ri1.execute-api.us-east-1.amazonaws.com/v1", stringbody
        )
        .then(function(response) {
          // eslint-disable-next-line
          console.log(response);
        //   if (response.data.success == true && log == "admin") {
        //     // eslint-disable-next-line
        //     router.push(
        //       "/f75778f7425be4db0369d09af37a6c2b9a83dea0e53e7bd57412e4b060e607f7"
        //     );
        //     console.log("Du är inloggad som admin");
        //   } else if (response.data.success == true) {
        //     router.push("/");
        //   }
        })
        .catch(function(error) {
          // eslint-disable-next-line
          console.log(error);
        });
    }
  }
};



// }
</script>

<style>
#a3 {
  font-size: 32px;
  text-align: center;
  font-family: "Arial";
}
#a4 {
  color: rgb(0, 0, 0);
  text-align: center;
}

#a5 {
  color: rgb(0, 0, 0);
}
</style>