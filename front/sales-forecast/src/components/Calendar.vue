import { GChart } from 'vue-google-charts'

<template>
<div id="chart">
<GChart
    :settings="{ packages: ['calendar'] }"
    type="Calendar"
    :data="chartData"
    :options="chartOptions"
  />
<h3>Location</h3>
<select v-model="active_filters.location" multiple>
  <option>1193</option>
  <option>500</option>
</select>
<h3>Product</h3>
<select v-model="active_filters.product" multiple>
  <option>1000</option>
  <option>500</option>
</select>
<h3>Event</h3>
<select v-model="active_filters.event" multiple>
  <option>1000</option>
  <option>500</option>
</select>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Calendar',
  data () {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        ['Date', 'Sales'],
        [new Date(2012, 3, 13), 1000],
        [new Date(2012, 3, 14), 1170],
        [new Date(2012, 3, 15), 660],
        [new Date(2012, 3, 16), 1030]
      ],
      chartOptions: {
        chart: {
          title: 'Sales Predicted',
          height: 500
        }
      },
      active_filters: {
        location: [],
        product: [],
        event: []
      },
      predictInfo: []
    }
  },
  methods: {
    getRecords () {
      const path = 'http://localhost:5000/api/v1.0/mensaje'
      axios.get(path).then((respuesta) => {
      	var obj = JSON.parse(respuesta.data)
      	for (var i = 0; i < obj.length; i++)
      	{
      	  console.log(obj[i].date)
      	  obj[i].date = new Date(obj[i].date)
          this.predictInfo.push(obj[i])
      	}
      })
        .catch((error) => {
          console.log(error)
        })
    },
    hasAttribute (record_attr, attribute_array) {
      if (!attribute_array.length > 0) return true
      if (!Array.isArray(record_attr)) return attribute_array.indexOf(record_attr) > -1
      return attribute_array.some(function (v) {
        return record_attr.indexOf(v) >= 0
      })
    }
  },
  created () {
    this.getRecords()
  },
  computed: {
    filtered_dates: function() {
      var data = this
      return data.predictInfo
        .filter(function(record){
          return data.hasAttribute(record.location, data.active_filters.location)
        })
        .filter(function(record){
          return data.hasAttribute(record.product, data.active_filters.product)
        })
        .filter(function(record){
          return data.hasAttribute(record.event, data.active_filters.event)
        })
    }
  }
}
</script>
