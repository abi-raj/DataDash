<template>
  <div>
    <div class="chart-options">
      <div class="class_y">
        <label for="choose_y">Choose Line : </label>
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
        type="line"
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
  name: "LineStep",
  components: {
    apexchart: VueApexCharts,
  },
  computed: {
    ...mapState(["fileData"]),
  },
  methods: {
    updateY(e) {
      this.$refs.real.updateSeries(
        [
          {
            name: e.target.value,
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
        {
          data: [],
        },
      ],

      chartOptions: {
        chart: {
          type: "line",
          height: 350,
        },
        stroke: {
          curve: "stepline",
        },
        dataLabels: {
          enabled: false,
        },
        title: {
          text: "Stepline Chart",
          align: "left",
        },
        markers: {
          hover: {
            sizeOffset: 4,
          },
        },
      },
    };
  },
};
</script>

<style >
.chart-options {
  @apply p-5 flex flex-row justify-around;
}
</style>