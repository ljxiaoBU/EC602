//Copyright 2017 Lijun Xiao ljxiao@bu.edu

#include <vector>


using namespace std;

typedef vector<double> Poly;



Poly add_poly(const Poly &a, const Poly &b) {
  Poly c;
  int i, j;
  int N;
  double sum;
  for(i = 0; i < a.size(); i++) {

    sum = a[i] + b[i];
    c.push_back(sum);
  }
  if(a.size() < b.size()) {
    for(i; i < b.size(); i++) {
      double t = b[i];
      c.push_back(t);
    }
  } else if(b.size() < a.size()) {
    for(i; i < a.size(); i++) {
      double q = a[i];
      c.push_back(q);
    }
  }

  N = c.size();
  N = N - 1;
  for(i = N; i > 0; i--) {
    if(c[i] == 0) {
      c.pop_back();
    } else
      break;
  }

  return c;
}



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


  int N = d.size();
  N = N - 1;
  for(i = N; i > 0; i--) {
    if(d[i] == 0) {
      d.pop_back();
    } else
      break;

  }

  return d;
}



