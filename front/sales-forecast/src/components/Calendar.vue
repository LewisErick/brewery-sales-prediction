import { GChart } from 'vue-google-charts'

<template>
<div id="chart">
<GChart
    :settings="{ packages: ['calendar'] }"
    type="Calendar"
    :data="chartData"
    :options="chartOptions"
  />
<br>
<div id="bar">
	<h3>Location</h3>
	<h4 v-on:click="clear_array('location')">Clear</h4>
	<select v-model="active_filters.location" multiple>
	  <option>136</option>
	  <option>152</option>
	  <option>1193</option>
	  <option>1258</option>
	  <option>1300</option>
	  <option>1355</option>
	</select>
	<h3>Product</h3>
	<h4 v-on:click="clear_array('product')">Clear</h4>
	<select v-model="active_filters.product" multiple>
	  <option>1</option>
	  <option>2</option>
	  <option>3</option>
	  <option>4</option>
	  <option>5</option>
	  <option>6</option>
	</select>
	<h3>Event</h3>
	<h4 v-on:click="clear_array('event')">Clear</h4>
	<select v-model="active_filters.event" multiple>
	  	<option>New Year's Eve</option>
		<option>2nd January (substitute day)</option>
		<option>Orthodox Christmas Day</option>
		<option>Orthodox New Year</option>
		<option>Burns Night</option>
		<option>Milad un Nabi (Mawlid)</option>
		<option>2nd January</option>
		<option>All Saints' Day </option>
		<option>All Souls' Day </option>
		<option>Ascension Day</option>
		<option>Ashura</option>
		<option>Assumption of Mary</option>
		<option>Battle of the Boyne</option>
		<option>Carnival/Ash Wednesday</option>
		<option>Carnival/Shrove Tuesday</option>
		<option>Epiphany</option>
		<option>Chinese New Year</option>
		<option>Christmas Day</option>
		<option>Christmas Eve</option>
		<option>Corpus Christi</option>
		<option>Daylight Saving Time ends</option>
		<option>Daylight Saving Time starts</option>
		<option>December Solstice</option>
		<option>Diwali/Deepavali</option>
		<option>Dussehra</option>
		<option>Early May Bank Holiday</option>
	</select>
</div>
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
      ],
      chartOptions: {
        chart: {
          title: 'Sales Predicted',
          height: 20000,
          calendar: { cellSize: 10 },
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
      	var str = respuesta.data.substring(0, respuesta.data.length - 1);
      	str = '[' + str + ']'
      	var obj = JSON.parse(str)
      	for (var i = 2; i < obj.length; i++)
      	{
      	  obj[i].date = new Date(obj[i].date)
          this.predictInfo.push(obj[i])
          this.chartData.push([obj[i].date,parseInt(obj[i].sa_quantity)])
      	}
      })
        .catch((error) => {
          console.log(error)
        })
    },
    hasAttribute (record_attr, attribute_array) {
      if (!attribute_array.length > 0) return true;
      if (!Array.isArray(record_attr)) return attribute_array.indexOf(record_attr) > -1;
      return attribute_array.some(function (v) {
        return record_attr.indexOf(v) >= 0;
      });
    },
    clear_array: function(array){
      this.active_filters[array] = [];
    }
  },
  created () {
    this.getRecords()
  },
  computed: {
    filtered_dates: function() {
      var data = this;
      return data.predictInfo
        .filter(function(record){
          return data.hasAttribute(record.location, data.active_filters.location)
        })
        .filter(function(record){
          return data.hasAttribute(record.product,data.active_filters.product)
        })
        .filter(function(record){
          return data.hasAttribute(record.event,data.active_filters.event)
        })
    }
  }
}
</script>