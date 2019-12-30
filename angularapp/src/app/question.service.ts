import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class QuestionService {

  getItems() {
    return this.http.get('http://localhost:8080/api/v1/rest/question/');
  }

  getSearch(q) {
    return this.http.get('http://localhost:8080/api/v1/rest/question/?q=' + q['search']);
  }

  getItem(id) {
    return this.http.get('http://localhost:8080/api/v1/rest/question/' + id)
  }

  addItem(data) {
    return this.http.post('http://localhost:8080/api/v1/rest/question/', data)
  }

  addAnswer(data) {
    return this.http.post('http://localhost:8080/api/v1/rest/answer/', data, {withCredentials: true})
  }

  constructor(
    private http: HttpClient
  ) {}

}
