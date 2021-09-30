<template>
  <div>
    <div class="prediction-options">
      <div class="class_x">
        <label for="choose_x">Choose X axis : </label>
        <select
          name="choose_x"
          id="choose_x"
          class="border-4 border-green-300"
          v-model="xCol"
          @change="updateX"
        >
          <option v-for="number in fileData.numCols" :key="number">
            {{ number }}
          </option>
        </select>
      </div>
      <div class="class_y">
        <label for="choose_y">Choose Y axis : </label>
        <select
          name="choose_y"
          id="choose_y"
          class="border-4 border-green-300"
          v-model="yCol"
          @change="updateY"
        >
          <option v-for="number in fileData.numCols" :key="number">
            {{ number }}
          </option>
        </select>
      </div>
    </div>

    <div
      class="
        flex flex-row
        space-x-5
        text-center
        center
      "
    >
      <label for="default" class="text-gray-700 select-none font-medium"
        >Value :
      </label>
      <input
        id="default"
        type="number"
        name="default"
        v-model="target"
        class="
          px-4
          py-2
          rounded-lg
          border border-gray-300
          focus:outline-none
          focus:ring-2 focus:ring-gray-200
          w-1/4
        "
      />
      <button class="btn-predict" @click="predictRequest">Predict</button>
    </div>
    <div class="res center">
      <p class="text-lg p-2">{{ result }}</p>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";
export default {
  name: "PredictionBase",
  computed: {
    ...mapState(["fileData"]),
  },
  data() {
    return {
      xCol: null,
      yCol: null,
      result: null,
      target: null,
    };
  },
  methods: {
    predictRequest() {
      if (this.xCol && this.yCol && this.target) {
        this.result = "Loading...";
        const formData = {
          x: this.fileData.allData[this.xCol],
          y: this.fileData.allData[this.yCol],
          target: this.target,
        };

        console.log(formData);
        axios
          .post(
            "https://CloudyPuzzledDominspector.abisnhss.repl.co/pred",
            formData
          )
          .then((response) => {
            console.log(response.data);
            this.result = "\nPredicted value is : "+response.data.result;
          })
          .catch((error) => {
            console.log(error);
            this.result = "Error occurred";
          });
      } else {
        this.result = "Please choose  all the values";
      }
    },
  },
};
</script>

<style >
.btn-predict {
  @apply px-4 py-2 rounded-md text-sm font-medium border-0 focus:outline-none focus:ring transition text-white bg-green-500 hover:bg-green-600 active:bg-green-700 focus:ring-green-300;
}
.prediction-options {
  @apply p-5 flex flex-row justify-center;
}
.center{
    @apply flex justify-center content-center;
}
</style>