function check(a, b, x, y, v) {
  let flag = false;
  for (let i = 0; i < x.length; i++) {
    if (Math.sqrt(Math.pow(x[i] - a, 2) + Math.pow(y[i] - b, 2)) <= r[i]) {
      flag = true;
    }
  }
  return flag;
}

function solution(x, y, r, v) {
  let [l, b, R, t] = [Infinity, Infinity, -Infinity, -Infinity];
  for (let i = 0; i < x.length; i++) {
    l = l > x[i] - r[i] ? x[i] - r[i] : l;
    b = b > y[i] - r[i] ? y[i] - r[i] : b;
    R = R < x[i] + r[i] ? x[i] + r[i] : R;
    t = t < y[i] + r[i] ? y[i] + r[i] : t;
  }
  let points = [];
  for (let i = 0; i < v.length; i += 2) {
    points.push([l + (v[i] % (R - l)), b + (v[i + 1] % (t - b))]);
  }
  result_points = points.filter((point) => {
    return check(point[0], point[1], x, y, r);
  });
  return Number((result_points.length / points.length) * (R - l) * (t - b));
}
const [x, y, r] = [[5], [5], [5]];
const v = [92, 83, 14, 45, 66, 37, 28, 9, 10, 81];
console.log(solution(x, y, r, v));
