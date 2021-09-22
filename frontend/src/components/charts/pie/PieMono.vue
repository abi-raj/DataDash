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
        type="pie"
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
  name: "PieMono",
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
      series: [25, 15, 44, 55, 41, 17],
      chartOptions: {
        chart: {
          width: "100%",
          type: "pie",
        },
        labels: [
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday",
        ],
        theme: {
          monochrome: {
            enabled: true,
          },
        },
        plotOptions: {
          pie: {
            dataLabels: {
              offset: -5,
            },
          },
        },
        title: {
          text: "Monochrome Pie",
        },
        dataLabels: {
          formatter(val, opts) {
            const name = opts.w.globals.labels[opts.seriesIndex];
            return [name, val.toFixed(1) + "%"];
          },
        },
        legend: {
          show: false,
        },
      },
    };
  },
};
</script>

<style >
</style>