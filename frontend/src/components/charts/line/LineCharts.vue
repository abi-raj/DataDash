<template>
  <div>
    <div class="all-charts">
      <div
        class="border-2 p-2 w-1/12"
        :class="{ 'border-green-300': choosen === 'basic' }"
        id="basic"
        @click="select('basic')"
      >
        Basic
      </div>
      <div
        class="border-2 p-2 w-1/12"
        :class="{ 'border-green-300': choosen === 'realtime' }"
        id="realtime"
        @click="select('realtime')"
      >
        Realtime
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LineCharts",
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
</style>