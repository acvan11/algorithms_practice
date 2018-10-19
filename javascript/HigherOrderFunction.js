const companies = [
  {name: "Company One", category: "Finance", start: 1981 , end: 2003 },
  {name: "Company Two", category: "Retail", start: 1992, end:  2008},
  {name: "Company Three", category: "Auto", start: 1999, end: 2007 },
  {name: "Company Four", category: "Retail", start: 2009, end: 2010 },
  {name: "Company Five", category: "Technology", start: 1987, end: 2014 },
  {name: "Company Six", category: "Finance", start: 1986 , end: 2010 },
  {name: "Company Seven", category: "Auto", start: 2011 , end:2016 },
  {name: "Company Eight", category: "Technology", start: 1981 , end: 1996},
  {name: "Company Nine", category: "Retail", start: 1981, end: 1989 },
];

const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];

for (let i = 0; i< companies.length; i++){
  console.log(companies[i])
}

forEach
companies.forEach( company => {
  console.log(company)
})

// filter
let canDrink = [];
for(let i = 0; i < ages.length; i++){
  if (ages[i] >= 21) {
    canDrink.push(ages[i]);
  }
}
console.log(canDrink)

const canDrink2 = ages.filter( age => age >= 21 )
console.log(canDrink2)

const retailCompanies = companies.filter(company => company.category === 'Retail')
console.log(retailCompanies)

// map
const ageMap = ages
.map(age => Math.sqrt(age))
.map(age => age*2);

console.log(ageMap)

// sort
const sortCompanies = companies.sort( (c1,c2) => {
  if (c1.start > c2.start) {
    return 1;
  }
  else {
    return -1;
  }
})

console.log(sortCompanies)
console.log(companies)

const sortAge = ages.sort( (a,b) => a-b)
console.log(sortAge)

// reduce

const ageSum = ages.reduce( (total, age) => total + age, 0)
console.log(ageSum)

const totalYear = companies.reduce( (total, company) => total + (company.end - company.start),0)
console.log(totalYear)