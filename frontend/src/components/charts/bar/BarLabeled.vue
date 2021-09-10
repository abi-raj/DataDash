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
  <div class="class_y">
        <label for="choose_y">Choose Y axis : </label>
        <select
          name="choose_y"
          id="choose_y"
          class="border-4 border-green-300"
          @change="updateY"
        >
          <option v-for="number in fileData.numCols" :key="number">
            {{ number }}
          </option>
        </select>
      </div>

      <div class="rstart">
        <label for="rstart">Range Start : </label>
        <input
          type="number"
          v-model="start"
          class="border-4 border-green-300"
        />
      </div>

      <div class="rend">
        <label for="rend">Range End : </label>
        <input type="number" v-model="end" class="border-4 border-green-300" />
      </div>
      </div>
    <div id="chart">
      <apexchart
      ref="real"
        type="bar"
        height="380"
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
  name: "BarLabeled",
  components: {
    apexchart: VueApexCharts,
  },
  computed: {
    ...mapState(["fileData"]),
  },
  methods: {
    updateX(e) {
      console.log(e.target.value, this.start, this.end);

      this.$refs.real.updateOptions({
        xaxis: {
          categories: this.fileData.allData[e.target.value].slice(
            this.start,
            this.end
          ),
        },
      });
    },
     updateY(e) {
      // console.log(e.target.value);
      // console.log(typeof this.fileData.allData[e.target.value]);
      // console.log(this.fileData.allData[e.target.value]);
      this.$refs.real.updateSeries(
        [
          {
            data: this.fileData.allData[e.target.value].slice(
              this.start,
              this.end
            ),
           
          },
        ],
        false,
        true
      );

   
    },
  },
  data() {
    return {
      start: 0,
      end: 20,
      series: [
        {
          data: [],
        },
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 380,
        },
        plotOptions: {
          bar: {
            barHeight: "100%",
            distributed: true,
            horizontal: true,
            dataLabels: {
              position: "bottom",
            },
          },
        },
        colors: [
          "#33b2df",
          "#546E7A",
          "#d4526e",
          "#13d8aa",
          "#A5978B",
          "#2b908f",
          "#f9a3a4",
          "#90ee7e",
          "#f48024",
          "#69d2e7",
        ],
        dataLabels: {
          enabled: true,
          textAnchor: "start",
          style: {
            colors: ["#fff"],
          },
          formatter: function (val, opt) {
            return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val;
          },
          offsetX: 0,
          dropShadow: {
            enabled: true,
          },
        },
        stroke: {
          width: 1,
          colors: ["#fff"],
        },
        xaxis: {
          categories: [],
        },
        yaxis: {
          labels: {
            show: false,
          },
        },
        title: {
          text: "Custom DataLabels",
          align: "center",
          floating: true,
        },
        subtitle: {
          text: "Category Names as DataLabels inside bars",
          align: "center",
        },
        tooltip: {
          theme: "dark",
          x: {
            show: false,
          },
          y: {
            title: {
              formatter: function () {
                return "";
              },
            },
          },
        },
      },
    };
  },
};
</script>

<style >
</style>