import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Injectable()
export class RestAuthService {
  token = '';
  constructor(private http: HttpClient) { }

    public isAuthenticated(): boolean {
    return Boolean(this.token);
    // return true;
  }

  public getAuthorizationString(): string {
    if (this.token) {
      return `Token ${ this.token }`;
    } else {
      return null;
    }
  }

  save(code, state) {
    localStorage.setItem('code', code);
    localStorage.setItem('state', state);
  }

  clear() {
    localStorage.removeItem('code');
    localStorage.removeItem('state');
  }

  isSaved() {
    return localStorage.getItem('code') && localStorage.getItem('state');
  }

    logout() {
      return this.http.get('http://localhost:8080/api/logout')
    }

    login(username, password) {
      return this.http.post('http://localhost:8080/api/login/',
        {'username': username, 'password': password})
    }

    socialLogin() {
      return this.http.post('http://localhost:8080/api/social-login/linkedin/',
        {code: localStorage.getItem('code'), state: localStorage.getItem('state')})
    }

    register(firstName, lastName, username, email, password1, password2) {
      return this.http.post('http://localhost:8080/api/rest-registration/',
        {'username': username, 'email': email, 'password1': password1, 'password2': password2})
    }
}


