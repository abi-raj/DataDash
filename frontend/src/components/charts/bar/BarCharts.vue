<template>
  <div>
    <div class="all-charts">
      <div
        class="border-2 p-2 w-1/12"
        :class="{ 'border-green-300': choosen === 'basic' }"
        id="basic"
        @click="select('basic')"
      >
        Basic
      </div>
      <div
        class="border-2 p-2 w-1/12"
        :class="{ 'border-green-300': choosen === 'grouped' }"
        id="grouped"
        @click="select('grouped')"
      >
        Grouped
      </div>
    </div>
    <BarBasic v-if="choosen === 'basic'" />
  </div>
</template>

<script>
import BarBasic from "./BarBasic.vue";
export default {
  name: "BarCharts",
  components: {
    BarBasic,
  },
  data() {
    return {
      choosen: null,
    };
  },
  methods: {
    select(name) {
      console.log("clicked");
      this.choosen = name;
    },
  },
};
</script>

<style >
</style>