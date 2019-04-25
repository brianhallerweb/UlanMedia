//@format
const moment = require('moment-timezone');

function calculateOneEightyDateRange() {
  today = moment()
    .tz('America/Los_Angeles')
    .format('YYYY-MM-DD');
  oneEightyDaysAgo = moment()
    .tz('America/Los_Angeles')
    .subtract(180, 'day')
    .format('YYYY-MM-DD');
  return [oneEightyDaysAgo, today];
}

console.log(calculateOneEightyDateRange());
