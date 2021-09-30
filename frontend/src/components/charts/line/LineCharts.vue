<template>
  <div>
    <div class="all-charts">
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'basic' }"
        id="basic"
        @click="select('basic')"
      >
        Basic
      </div>
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'stepline' }"
        id="stepline"
        @click="select('stepline')"
      >
        Step Line
      </div>
      <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'labeled' }"
        id="labeled"
        @click="select('labeled')"
      >
        Labeled
      </div>
    </div>
    <div class="charts">
      <LineBasic v-if="choosen === 'basic'" />
      <LineStep v-if="choosen === 'stepline'" />
      <LineLabeled v-if="choosen === 'labeled'" />
    </div>
  </div>
</template>

<script>
import LineBasic from "./LineBasic.vue";
import LineStep from "./LineStep.vue";
import LineLabeled from "./LineLabeled.vue";
export default {
  name: "LineCharts",
  components: {
    LineBasic,
    LineStep,
    LineLabeled,
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
.chart-select {
  @apply border-2 p-2 w-1/12 text-center;
}
.all-charts {
  @apply p-4 flex justify-around;
}
</style>