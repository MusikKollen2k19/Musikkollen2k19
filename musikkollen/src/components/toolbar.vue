<template>
  <div>
    <v-app-bar color="primary">
      <v-img
        class="shrink mt-1 hidden-sm-and-down"
        contain
        min-width="100"
        src="@/assets/AbbInduMH.png"
        width="100"
      />

      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-btn v-for="(link, i) in links" :key="i" :to="link.path" color="primary">{{link.name}}</v-btn>

      <v-btn href="https://sverigesradio.se/musikhjalpen" target="_blank" text>
        <span class="mr-2">MUSIKHÄLPEN</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
      </v-toolbar-items>
    </v-app-bar>
  </div>
</template>

<script>
import paths from "@/router/paths";

export default {
  data: () => ({}),
  computed: {
    links() {
      return paths;
    }
  }
};
</script>