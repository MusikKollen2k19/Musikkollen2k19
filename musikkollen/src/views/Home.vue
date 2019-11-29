<template>
  <div>
    <v-row align="center" justify="center">
      <Hem />
      <!-- <testcard /> -->
      <Chart />
    </v-row>
  </div>
</template>
 
<script>
export default {
  name: "HomePage",
  components: {
    Hem: () => import("../components/Hem.vue"),
    Chart: () => import("../components/Chart.vue")
    // testcard: () => import("../components/testcard.vue")
  }
};
</script>