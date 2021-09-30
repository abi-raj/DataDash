<template>
  <div class="container mx-auto p-10">
    <div class="w-auto flex flex-row justify-between">
      <div><h2 class="text-xl">3) Choose a Chart</h2></div>
      <div>
        <select class="border-4 border-green-300" v-model="chartType">
          <option value="bar">Bar Charts</option>
          <option value="line">Line Charts</option>
          <option value="column">Column Charts</option>
          <option value="area">Area Charts</option>
          <option value="pie">Pie Charts</option>
        </select>
      </div>
    </div>
    <div v-if="chartType">
      <BarChart v-if="chartType === 'bar'" />
      <LineChart v-if="chartType === 'line'" />
      <ColumnChart v-if="chartType === 'column'" />
      <AreaChart v-if="chartType === 'area'" />
      <PieChart v-if="chartType === 'pie'" />
    </div>
  </div>
</template>

<script>
import BarChart from "./bar/BarCharts.vue";
import LineChart from "./line/LineCharts.vue";
import ColumnChart from "./column/ColumnCharts.vue";
import AreaChart from "./area/AreaCharts.vue";
import PieChart from "./pie/PieCharts.vue";
export default {
  name: "ChooseChart",
  data() {
    return {
      chartType: null,
    };
  },
  components: {
    BarChart,
    LineChart,
    ColumnChart,
    AreaChart,
    PieChart,
  },
};
</script>

<style>
</style>