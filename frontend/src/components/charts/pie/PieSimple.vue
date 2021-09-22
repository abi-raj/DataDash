<template>
  <div>
    <div class="chart-options">
      <div class="class_x">
        <label for="choose_x">Choose X axis : </label>
        <select
          name="choose_x"
          id="choose_x"
          class="border-4 border-green-300"
          @change="updateX"
        >
          <option v-for="str in fileData.strCols" :key="str">
            {{ str }}
          </option>
        </select>
      </div>
    </div>
    <button class="btn" @click="download()">Render</button>
    <a :href="imageDownload" download>Download</a>
    <div id="chart">
      <apexchart
        ref="real"
        height="350"
        type="donut"
        :options="chartOptions"
        :series="series"
      ></apexchart>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";
import { mapState } from "vuex";
export default {
  name: "PieSimple",
  components: {
    apexchart: VueApexCharts,
  },
  computed: {
    ...mapState(["fileData"]),
  },
  methods: {
    async download() {
      let el = this.$refs.real.$el;
      let options = { type: "dataURL" };
      this.imageDownload = await this.$html2canvas(el, options);
      //console.log(typeof this.imageDownload)
    },
  },
  data() {
    return {
      imageDownload: null,
      series: [44, 55, 13, 43, 22],
      chartOptions: {
        chart: {
          width: 380,
          type: "pie",
        },
        labels: ["Team A", "Team B", "Team C", "Team D", "Team E"],
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200,
              },
              legend: {
                position: "bottom",
              },
            },
          },
        ],
      },
    };
  },
};
</script>

<style >
</style>