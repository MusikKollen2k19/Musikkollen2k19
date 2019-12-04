<template>
  <v-app id="background" fixed>
    <v-flex justify-center align-center>
      <v-card max-width="450" elevation="20" justify-center align-center class-mx-auto id="a6">
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
            <span>Du kan lägga till ett minustecken för att ta bort en summa</span>
          <v-card-actions>
            <v-row>
              <v-btn
                :disabled="!valid || dis"
                :loading="dis"
                id="a5"
                
                color="primary"
                block
                tile
                @click="submit"
              >Lägg till</v-btn>
            </v-row>
          </v-card-actions>
          <br />
          <v-alert :type="Alert_type" v-if="Alert">{{ Alert_text }}</v-alert>
        </v-card-text>
      </v-card>
    </v-flex>
    <v-snackbar v-model="snackbar">
      {{ snackbar_text }}
      <v-btn :color="snackbar_type" text @click="snackbar = false">Close</v-btn>
    </v-snackbar>
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
    dis: false,
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
      v => (v && typeof v != "number") || "Inte ett Nummer!"
    ],
    snackbar: false,
    snackbar_text: "Fail!",
    snackbar_type: "success",
    Alert: false,
    Alert_text: "Fail!",
    Alert_type: "success"
  }),
  methods: {
    async submit() {
      this.dis = true;
      var log = this.login;
      let body = {
        user: this.login,
        pass: sha256(this.password),
        Amount: parseInt(this.sek)
      };
      let stringbody = JSON.stringify(body);
      console.log(stringbody);
      const response = await axios.post(
        "https://km1wzv5ri1.execute-api.us-east-1.amazonaws.com/v1",
        stringbody
      );
      // eslint-disable-next-line
      this.Alert = true;
      this.Alert_text = response.data.Meddelande;
      this.snackbar = true;
      this.snackbar_text = response.data.Meddelande;
      if (response.data.Success == true) {
        this.Alert_type = "success";
        this.snackbar_type = "success";
      } else {
        this.Alert_type = "error";
        this.snackbar_type = "error";
      }
      this.dis = false;
      // this.snackbar = true;
      // router.push("/");
    }
  }
};
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