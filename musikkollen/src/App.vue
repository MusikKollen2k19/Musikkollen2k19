<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="@/assets/AbbInduMH.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://sverigesradio.se/musikhjalpen"
        target="_blank"
        text
      >
        <span class="mr-2">MUSIKHÄLPEN</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <Hem/>
      <Chart />
    </v-content>
  </v-app>
</template>

<script>
import Hem from './components/Hem';
import Chart from "./components/Chart";

export default {
  name: 'App',

  components: {
    Hem,
    Chart,
  },

  data: () => ({
    //
  }),
};
</script>
