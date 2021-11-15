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
import {mapState} from 'vuex';
export default {
  name: "ColumnBasic",
  components: {
    apexchart: VueApexCharts,
  },
  computed:{
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
      start:0,
      end:15,
      choosenCol: null,
      addedColumns: [],
      addedColVals: [],
      series: [
      ],
      chartOptions: {
        chart: {
          type: "bar",
          height: 350,
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "55%",
            endingShape: "rounded",
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          show: true,
          width: 2,
          colors: ["transparent"],
        },
        xaxis: {
          categories: [        
          ],
        },
        yaxis: {
          title: {
            text: "",
          },
        },
        fill: {
          opacity: 1,
        },
        // tooltip: {
        //   y: {
        //     formatter: function (val) {
        //       return "$ " + val + " thousands";
        //     },
        //   },
        // },
      },
    };
  },
};
</script>

<style >
</style>