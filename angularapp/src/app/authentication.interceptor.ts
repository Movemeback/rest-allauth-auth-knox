import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { RestAuthService } from './restauth.service';

/**
 * Simple interceptor to append Authorization header to the every request header is user is authenticated.
 */
@Injectable()
export class AuthenticationInterceptor implements HttpInterceptor {

  constructor(private authenticationService: RestAuthService) {}

  intercept (req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (this.authenticationService.isAuthenticated()) {
      const authReq = req.clone({
        headers: req.headers.set('Authorization', this.authenticationService.getAuthorizationString())
      });
      return next.handle(authReq);
    } else {
      return next.handle(req);
    }

  }
}
