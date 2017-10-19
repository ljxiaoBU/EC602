//Copyright 2017 Lijun Xiao ljxiao@bu.edu
#include <string>
#include <vector>
using namespace std;

typedef string BigInt;
typedef vector<int> Poly;


Poly multiply_poly(const Poly &a, const Poly &b) {
  int i, m, n, len;
  len = a.size() + b.size() - 1;
  Poly d(len, 0);
  for(i = 0; i <= (a.size() + b.size() - 1); i++) {
    for(m = 0; m < a.size(); m++) {
      for(n = 0; n < b.size(); n++) {
        if(m + n == i) {
          d[i] = d[i] + a[m] * b[n];

        }
      }
    };

  }
  return d;
}

BigInt multiply_int(const BigInt &a, const BigInt &b) {

  Poly z, mul;
  Poly m, n;

  for(int i = 0; i < a.size(); i++) {
    m.push_back(a[i] - '0');

  }

  for(int i = 0; i < b.size(); i++) {
    n.push_back(b[i] - '0');

  }

  mul = multiply_poly(m, n);
  int chu = 0;
  int bianliang = 0;
  int yushu = 0;
  for(int i = (mul.size() - 1); i >= 0; i--) {

    bianliang = mul[i] + chu;
    chu = bianliang / 10;
    yushu = bianliang % 10;
    z.push_back(yushu);

  }
  if(chu != 0) {
    z.push_back(chu);
  }
  BigInt str;
  if(z[z.size() - 1] == 0) {
    for(int i = (z.size() - 1); i > 0; i--) {
      z.pop_back();
    }

  }
  for(int i = (z.size() - 1); i >= 0; i--) {
    str = str + to_string(z[i]);

  }

  return str;
}