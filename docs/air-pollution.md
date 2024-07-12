---
title: Air Pollution
toc: false
---

```js
let data = await FileAttachment("data/air-pollution.csv").csv({typed: true})

data = data.flatMap(d => {
    d.City = d.City.replace(' (metropolitan area)', '')
    d.City = d.City.replace('Metropolitan Association of ', '')
    return d
  })
```

<div class='card'>

```js
const pm2005desc = data.sort((a, b) => d3.descending(a['Avoidable deaths [WHO 2005 levels] [PM2.5]'], b['Avoidable deaths [WHO 2005 levels] [PM2.5]']))
```

```js
const topCities = pm2005desc.slice(0, 10)
const cityNames1 = topCities.map(d => d.City);
```

```js
const height = 600
const marginBottom = 30
const marginTop = 100
const marginRight = 30
const marginLeft = 80

const svg = d3.create('svg')
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", [0, 0, width, height])
  .attr("style", "max-width: 100%; height: auto; font: sans-serif;")

const headline = svg.append('text')
  .attr('transform', `translate(80, 40)`)
  .attr('font-size', 20)
  .text('Avoidable deaths (WHO 2005 levels) [PM2.5] - top 10')

const x = d3.scaleLinear()
  .domain(d3.extent(data, d => d['Avoidable deaths [WHO 2005 levels] [PM2.5]']))
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
  .data(topCities)
  .join("rect")
    .attr("x", x(0))
    .attr("y", d => y(d.City))
    .attr("width", d => x(d['Avoidable deaths [WHO 2005 levels] [PM2.5]']) - x(0))
    .attr("height", y.bandwidth());

const chartA = svg.node()
```
  <div>${chartA}</div>
</div>

<div class='card'>

```js
//const pm2005asc = data.sort((a, b) => d3.ascending(a['Avoidable deaths [WHO 2005 levels] [PM2.5]'], b['Avoidable deaths [WHO 2005 levels] [PM2.5]']))
//const bottomCities = pm2005asc.slice(0, 10)
//const cityNames2 = bottomCities.map(d => d.City);

//const citiesWithZeroValue = data.filter(d => d['Avoidable deaths [WHO 2005 levels] [PM2.5]'] === 0);

// 128 cities
//const cityNamesWithZeroValue = citiesWithZeroValue.map(d => d.City);
```

```js
const pm2021desc = data.sort((a, b) => d3.descending(a['Avoidable deaths [WHO 2021 levels] [PM2.5]'], b['Avoidable deaths [WHO 2021 levels] [PM2.5]']))
const topCities2 = pm2021desc.slice(0, 10)
const cityNames2 = topCities2.map(d => d.City);
```

```js
const height = 600
const marginBottom = 30
const marginTop = 100
const marginRight = 30
const marginLeft = 80

const svg = d3.create('svg')
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", [0, 0, width, height])
  .attr("style", "max-width: 100%; height: auto; font: sans-serif;")

const headline = svg.append('text')
  .attr('transform', `translate(80, 40)`)
  .attr('font-size', 20)
  .text('Avoidable deaths [WHO 2021 levels] [PM2.5] - top 10')

const x = d3.scaleLinear()
  .domain(d3.extent(data, d => d['Avoidable deaths [WHO 2021 levels] [PM2.5]']))
  .nice()
  .range([marginLeft, width - marginRight])

const y = d3.scaleBand()
  .domain(cityNames2)
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
  .data(topCities2)
  .join("rect")
    .attr("x", x(0))
    .attr("y", d => y(d.City))
    .attr("width", d => x(d['Avoidable deaths [WHO 2021 levels] [PM2.5]']) - x(0))
    .attr("height", y.bandwidth());

const chartB = svg.node()
```
  <div>${chartB}</div>
</div>


<div class='card'>

```js
const no2desc2005 = data.sort((a, b) => d3.descending(a['Avoidable deaths [WHO 2005 levels] [NO2]'], b['Avoidable deaths [WHO 2005 levels] [NO2]']))
const topCities3 = no2desc2005.slice(0, 10)
const cityNames3 = topCities3.map(d => d.City);
```

```js
const height = 600
const marginBottom = 30
const marginTop = 100
const marginRight = 30
const marginLeft = 80

const svg = d3.create('svg')
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", [0, 0, width, height])
  .attr("style", "max-width: 100%; height: auto; font: sans-serif;")

const headline = svg.append('text')
  .attr('transform', `translate(80, 40)`)
  .attr('font-size', 20)
  .text('Avoidable deaths [WHO 2005 levels] [NO2] - top 10')

const x = d3.scaleLinear()
  .domain(d3.extent(data, d => d['Avoidable deaths [WHO 2005 levels] [NO2]']))
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
    .attr("width", d => x(d['Avoidable deaths [WHO 2005 levels] [NO2]']) - x(0))
    .attr("height", y.bandwidth());

const chartC = svg.node()
```
  <div>${chartC}</div>
</div>


<div class='card'>

```js
const no2desc2021 = data.sort((a, b) => d3.descending(a['Avoidable deaths [WHO 2021 levels] [NO2]'], b['Avoidable deaths [WHO 2021 levels] [NO2]']))
const topCities4 = no2desc2021.slice(0, 10)
const cityNames4 = topCities4.map(d => d.City);
```

```js
const height = 600
const marginBottom = 30
const marginTop = 100
const marginRight = 30
const marginLeft = 80

const svg = d3.create('svg')
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", [0, 0, width, height])
  .attr("style", "max-width: 100%; height: auto; font: sans-serif;")

const headline = svg.append('text')
  .attr('transform', `translate(80, 40)`)
  .attr('font-size', 20)
  .text('Avoidable deaths [WHO 2021 levels] [NO2] - top 10')

const x = d3.scaleLinear()
  .domain(d3.extent(data, d => d['Avoidable deaths [WHO 2021 levels] [NO2]']))
  .nice()
  .range([marginLeft, width - marginRight])

const y = d3.scaleBand()
  .domain(cityNames4)
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
  .data(topCities4)
  .join("rect")
    .attr("x", x(0))
    .attr("y", d => y(d.City))
    .attr("width", d => x(d['Avoidable deaths [WHO 2021 levels] [NO2]']) - x(0))
    .attr("height", y.bandwidth());

const chartD = svg.node()
```
  <div>${chartD}</div>
</div>
