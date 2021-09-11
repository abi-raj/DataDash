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

      <div class="add-cols">
        <label for="add_cols">Choose to add : </label>
        <select
          name="choose_y"
          id="choose_y"
          class="border-4 border-green-300"
          v-model="choosenCol"
        >
          <option v-for="number in fileData.numCols" :key="number">
            {{ number }}
          </option>
        </select>
      </div>
      <div class="add-btn">
        <button
          class="
            bg-green-500
            hover:bg-green-700
            text-white
            font-bold
            text-sm
            p-2
            rounded
          "
          @click="addCols"
        >
          Add
        </button>
      </div>
      <div class="added-cols">
        <label for="add_cols">Labels Picked : </label>
        <select
          name="choose_custom"
          id="choose_custom"
          class="border-4 border-green-300"
        >
          <option v-for="cols in addedColumns" :key="cols">
            {{ cols }}
          </option>
        </select>
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
  name: "LineLabeled",
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
    updateY() {
      this.$refs.real.updateSeries(this.addedColVals, false, true);
    },
    addCols() {
      if (
        this.choosenCol != null &&
        !this.addedColumns.includes(this.choosenCol)
      ) {
        this.addedColumns.push(this.choosenCol);
        this.addedColVals.push({
          name: this.choosenCol,
          data: this.fileData.allData[this.choosenCol].slice(
            this.start,
            this.end
          ),
        });
        this.updateY();
      }
    },
  },
  data() {
    return {
      start: 0,
      end: 15,
      choosenCol: null,
      addedColumns: [],
      addedColVals: [],
      series: [
      
      ],
      chartOptions: {
        chart: {
          height: 550,
          type: "line",
          dropShadow: {
            enabled: true,
            color: "#000",
            top: 18,
            left: 7,
            blur: 10,
            opacity: 0.2,
          },
          toolbar: {
            show: false,
          },
        },
        colors: ["#77B6EA", "#545454"],
        dataLabels: {
          enabled: true,
        },
        stroke: {
          curve: "smooth",
        },
        title: {
          text: "Average High & Low Temperature",
          align: "left",
        },
        grid: {
          borderColor: "#e7e7e7",
          row: {
            colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
            opacity: 0.5,
          },
        },
        markers: {
          size: 1,
        },
        xaxis: {
          categories: [],
          title: {
            text: "Month",
          },
        },
        yaxis: {
          title: {
            text: "Temperature",
          },
          min: 5,
          max: 40,
        },
        legend: {
          position: "top",
          horizontalAlign: "right",
          floating: true,
          offsetY: -25,
          offsetX: -5,
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