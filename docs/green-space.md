---
title: Green space
toc: false
---

```js
let data = await FileAttachment("data/green-space.csv").csv({typed: true})

data = data.flatMap(d => {
    d.City = d.City.replace(' (metropolitan area)', '')
    d.City = d.City.replace('Metropolitan Association of ', '')
    return d
  })
```

<div class='card'>

```js
const populationBelowTarget = data.sort((a, b) => d3.descending(a['% Population below %GA target [%GA]'], b['% Population below %GA target [%GA]']))
```

```js
const topCities1 = populationBelowTarget.slice(0, 10)
const cityNames1 = topCities1.map(d => d.City);
```

```js
const height = 600
const marginBottom = 30
const marginTop = 100
const marginRight = 30
const marginLeft = 300

const svg = d3.create('svg')
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", [0, 0, width, height])
  .attr("style", "max-width: 100%; height: auto; font: sans-serif;")

const headline = svg.append('text')
  .attr('transform', `translate(40, 40)`)
  .attr('font-size', 20)
  .text('% Population below %GA target [%GA] - top 10')

const x = d3.scaleLinear()
  .domain(d3.extent(data, d => d['% Population below %GA target [%GA]']))
  .nice()
  .range([marginLeft, width - marginRight])

const y = d3.scaleBand()
  .domain(cityNames1)
  .range([marginTop, height - marginBottom])
  .padding(0.1)

const xAxis = svg.append('g')
  .attr("transform", `translate(0,${marginTop})`)
  .call(d3.axisTop(x))

const yAxis = svg.append('g')
  .attr('transform', `translate(${marginLeft},0)`)
  .call(d3.axisLeft(y))

const rect = svg.append("g")
    .attr("fill", "steelblue")
  .selectAll('rect')
  .data(topCities1)
  .join("rect")
    .attr("x", x(0))
    .attr("y", d => y(d.City))
    .attr("width", d => x(d['% Population below %GA target [%GA]']) - x(0))
    .attr("height", y.bandwidth());

const chartA = svg.node()
```
  <div>${chartA}</div>
</div>

<div class='card'>

```js
const populationOverTarget = data.sort((a, b) => d3.ascending(a['% Population below %GA target [%GA]'], b['% Population below %GA target [%GA]']))
const topCities2 = populationOverTarget.slice(0, 10)
const cityNames2 = topCities2.map(d => d.City);
```

```js
const height = 600
const marginBottom = 30
const marginTop = 100
const marginRight = 30
const marginLeft = 100

const svg = d3.create('svg')
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", [0, 0, width, height])
  .attr("style", "max-width: 100%; height: auto; font: sans-serif;")

const headline = svg.append('text')
  .attr('transform', `translate(40, 40)`)
  .attr('font-size', 20)
  .text('% Population below %GA target [%GA] - lowest 10 cities')

const x = d3.scaleLinear()
  .domain(d3.extent(data, d => d['% Population below %GA target [%GA]']))
  .nice()
  .range([marginLeft, width - marginRight])

const y = d3.scaleBand()
  .domain(cityNames2)
  .range([height - marginBottom, marginTop])
  .padding(0.1)

const xAxis = svg.append('g')
  .attr("transform", `translate(0,${marginTop})`)
  .call(d3.axisTop(x))

const yAxis = svg.append('g')
  .attr('transform', `translate(${marginLeft},0)`)
  .call(d3.axisLeft(y))

const rect = svg.append("g")
    .attr("fill", "steelblue")
  .selectAll('rect')
  .data(topCities2)
  .join("rect")
    .attr("x", x(0))
    .attr("y", d => y(d.City))
    .attr("width", d => x(d['% Population below %GA target [%GA]']) - x(0))
    .attr("height", y.bandwidth());

const chartB = svg.node()
```
  <div>${chartB}</div>
</div>

<div class='card'>

```js
const avoidableDeathsPercent = data.sort((a, b) => d3.descending(a['Avoidable deaths [%GA target] [%GA]'], b['Avoidable deaths [%GA target] [%GA]']))
const topCities3 = avoidableDeathsPercent.slice(0, 10)
const cityNames3 = topCities3.map(d => d.City);

const height = 600
const marginBottom = 30
const marginTop = 100
const marginRight = 30
const marginLeft = 100

const svg = d3.create('svg')
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", [0, 0, width, height])
  .attr("style", "max-width: 100%; height: auto; font: sans-serif;")

const headline = svg.append('text')
  .attr('transform', `translate(40, 40)`)
  .attr('font-size', 20)
  .text('Avoidable deaths [%GA target] [%GA] - top 10')

const x = d3.scaleLinear()
  .domain(d3.extent(data, d => d['Avoidable deaths [%GA target] [%GA]']))
  .nice()
  .range([marginLeft, width - marginRight])

const y = d3.scaleBand()
  .domain(cityNames3)
  .range([marginTop, height - marginBottom])
  .padding(0.1)

const xAxis = svg.append('g')
  .attr("transform", `translate(0,${marginTop})`)
  .call(d3.axisTop(x))

const yAxis = svg.append('g')
  .attr('transform', `translate(${marginLeft},0)`)
  .call(d3.axisLeft(y))

const rect = svg.append("g")
    .attr("fill", "steelblue")
  .selectAll('rect')
  .data(topCities3)
  .join("rect")
    .attr("x", x(0))
    .attr("y", d => y(d.City))
    .attr("width", d => x(d['Avoidable deaths [%GA target] [%GA]']) - x(0))
    .attr("height", y.bandwidth());

const chartC = svg.node()
```
  <div>${chartC}</div>
</div>

