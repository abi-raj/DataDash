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
        height="350"
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
  name: "ColumnDataLabeled",
  components: {
    apexchart: VueApexCharts,
  },
  computed: {
    ...mapState(["fileData"]),
  },
   methods: {
    updateX(e) {
      console.log(this.start, this.end);

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
      this.$refs.real.updateSeries(
        [
          {
            name:e.target.value,
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
      end: 15,
      series: [
      
      ],
      chartOptions: {
        chart: {
          height: 350,
          type: "bar",
        },
        plotOptions: {
          bar: {
            borderRadius: 10,
            dataLabels: {
              position: "top", // top, center, bottom
            },
          },
        },
        dataLabels: {
          enabled: true,
          formatter: function (val) {
            return val + "%";
          },
          offsetY: -20,
          style: {
            fontSize: "12px",
            colors: ["#304758"],
          },
        },

        xaxis: {
          categories: [
            
          ],
          position: "top",
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
          crosshairs: {
            fill: {
              type: "gradient",
              gradient: {
                colorFrom: "#D8E3F0",
                colorTo: "#BED1E6",
                stops: [0, 100],
                opacityFrom: 0.4,
                opacityTo: 0.5,
              },
            },
          },
          tooltip: {
            enabled: true,
          },
        },
        yaxis: {
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
          labels: {
            show: false,
            formatter: function (val) {
              return val + "%";
            },
          },
        },
        title: {
          text: "Monthly Inflation in Argentina, 2002",
          floating: true,
          offsetY: 330,
          align: "center",
          style: {
            color: "#444",
          },
        },
      },
    };
  },
};
</script>

<style >
</style>