let n = Number(require("fs").readFileSync("/dev/stdin").toString().trim());
let num = 666;
let count = 1;
while (count != n) {
    num++;
    if (String(num).includes("666")) count++;
}

console.log(num);