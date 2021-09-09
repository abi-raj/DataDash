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
        :class="{ 'border-green-300': choosen === 'labels' }"
        id="labels"
        @click="select('labels')"
      >
        Data labels
      </div>
       <div
        class="chart-select"
        :class="{ 'border-green-300': choosen === 'distributed' }"
        id="distributed"
        @click="select('distributed')"
      >
        Distributed
      </div>
    </div>
    <div class="charts">
<ColumnBasic v-if="choosen==='basic'"/>
<ColumnDatalabeled v-if="choosen==='labels'"/>
<ColumnDistributed v-if="choosen==='distributed'"/>
    </div>
  </div>
</template>

<script>
import ColumnBasic from "./ColumnBasic.vue";
import ColumnDatalabeled from "./ColumnDatalabeled.vue";
import ColumnDistributed from "./ColumnDistributed.vue";
export default {
  name: "ColumnCharts",
  components: {
    ColumnBasic,
    ColumnDatalabeled,
    ColumnDistributed
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
.chart-select{
  @apply border-2 p-2 w-1/12 text-center;
}
.all-charts{
  @apply p-4 flex justify-around;
}
</style>