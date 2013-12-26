/*
 * =====================================================================================
 *
 *       Filename:  pagerank.cpp
 *
 *    Description:  Yet another implementation of the Pagerank algorithm.
 *
 *        Version:  1.0
 *        Created:  12/26/2013 05:00:21 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Osman Baskaya
 *        Company:  AIKU
 *
 * =====================================================================================
 */

// reading a text file
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <math.h> 

using namespace std;

map<string, vector<string> > IN_LINKS;
map<string, vector<string> > OUT_LINKS;
set <string> SINKS;
set <string> PAGES;

typedef std::pair<string, double> MyPair;
struct CompareByKey {
  bool operator() (const MyPair& a, const MyPair& b) const {
    return a.first < b.first;
  };
};
struct CompareByValue {
  bool operator() (const MyPair& a, const MyPair& b) const {
    return a.second < b.second;
  };
};

vector< MyPair > map_sort(map <string, double> map) {
  vector< MyPair > mapcopy(map.begin(), map.end());
  sort(mapcopy.begin(), mapcopy.end(), CompareByValue());
  return mapcopy;
}

double entropy_score(map<string, double> map){
  double e, s;
  for(auto outer_iter=map.begin(); outer_iter!=map.end(); ++outer_iter) {
    string p = outer_iter->first;
    s = outer_iter->second;
    e += -s * log2(s);
  }
  return pow(2, e);
}

void clean_sink() {
  for(auto outer_iter=OUT_LINKS.begin(); outer_iter!=OUT_LINKS.end(); ++outer_iter) {
    SINKS.erase(outer_iter->first);
  }
}

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
  std::stringstream ss(s);
  std::string item;
  while (std::getline(ss, item, delim)) {
    elems.push_back(item);
  }
  return elems;
}

std::vector<std::string> split(const std::string &s, char delim) {
  std::vector<std::string> elems;
  split(s, delim, elems);
  return elems;
}

void process_input(ifstream &myfile) {
  string line;
  if (myfile.is_open()) {
    while (getline(myfile,line)) {
      vector<string> tokens = split(line, ' ');
      vector<string> inlinks;
      //for ( auto &i : tokens ) {
      string head = tokens.at(0);
      PAGES.insert(head);
      SINKS.insert(head); // we will clean this later
      IN_LINKS[head] = inlinks;
      for (size_t i=1; i < tokens.size(); i++){
        string p = tokens[i];
        IN_LINKS[head].push_back(p);
        if (OUT_LINKS.find(p) == OUT_LINKS.end()) {
          vector <string> outlinks;
          OUT_LINKS[p] = outlinks;
        }
        OUT_LINKS[p].push_back(p);
      }
    }
    myfile.close();
    clean_sink();
    }
    else cout << "Unable to open file"; 
}

map<string, double> page_rank_init(double d) {
  string p;
  map<string, double> PR;
  map<string, double> newPR;
  int N = PAGES.size();
  double initial_prob = 1.0 / N;
  for(auto outer_iter=PAGES.begin(); outer_iter!=PAGES.end(); ++outer_iter) {
    p = *outer_iter;
    PR[p] = initial_prob;
    //cout << p << ":\t" << PR[p] << endl; 
  }

  int epoch = 0;
  int converge_count = 0;
  double prev_entropy = 0;
  //for (unsigned int i=0; i<100; i++) {
  cerr << setprecision(9);
  while (converge_count <= 4) {
    double sinkPR = 0;
    double e = entropy_score(PR);

    // Convergence Test
    if (abs(prev_entropy - e) < 0.0001) converge_count++;
    else converge_count = 0;
    cerr << "Epoch " << epoch << ":\t" << setw(9) << e << endl;
    for(auto outer_iter=SINKS.begin(); outer_iter!=SINKS.end(); ++outer_iter) {
      p = *outer_iter;
      sinkPR += PR[p];
    }
    for(auto outer_iter=PAGES.begin(); outer_iter!=PAGES.end(); ++outer_iter) {
      p = *outer_iter;
      newPR[p] = (1-d) / N;
      newPR[p] += d*sinkPR / N;
      vector <string> inlinks = IN_LINKS[p];
      //cout << "head: " << p << endl;
      for (size_t i=0; i < inlinks.size(); i++){
        string q = inlinks[i];
        newPR[p] += d * PR[q] / OUT_LINKS[q].size();
        //cout << "\tinlinks: " << q << endl;
      }
    }
    for(auto outer_iter=newPR.begin(); outer_iter!=newPR.end(); ++outer_iter) {
      p = outer_iter->first;
      double score = outer_iter->second;
      PR[p] = score;
    }
    epoch++;
    prev_entropy = e;
  }
  return PR;
}

int main (int argc, char *argv[]) {

  double d = atof(argv[2]); // Damping Factor
  ifstream myfile (argv[1]);
  process_input(myfile);
  cerr << "Reading done" << endl;
  map<string, double> PR = page_rank_init(d);
  cerr << "Pagerank Algorithm is converged" << endl;
  vector< MyPair > pairs = map_sort(PR);
  for (unsigned i = pairs.size(); i-- > 0;){
    MyPair pair = pairs[i];
    cout << pair.first << " score:\t" << pair.second << endl;
  }
  
  //for(auto outer_iter=PR.begin(); outer_iter!=PR.end(); ++outer_iter) {
    //string p = outer_iter->first;
    //double s = outer_iter->second;
    //cout << "Page: " << p << " :\t" << s << endl;
  //}

  return 0;
}
