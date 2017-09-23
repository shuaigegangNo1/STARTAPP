/**
 * Created by huangxuewen on 2017/9/16.
 */
import {Injectable} from "@angular/core";
import {AlertController} from "ionic-angular";
import {Http} from "@angular/http"
import {BaseService} from "./baseService";
import {person} from "../model/person";
@Injectable()
export class PersonService extends BaseService{

  constructor(public alertCtrl: AlertController, private http: Http) {
    super(alertCtrl);
  }

  getServiceUrl(){
    //return 'http://0.0.0.0:5000';
    return 'http://192.168.0.101:5000'
    //return 'http://192.168.2.141:5000'
  }
  getPersonList() {
    return this.http.get(this.getServiceUrl() + '/momApp/persons').map(res => res.json()).catch(this.handleError);
  }
  createPerson(person: person) {
    return this.http.post(this.getServiceUrl()+'/momApp/addPerson',JSON.stringify(person)).map(res => res.json()).catch(this.handleError);
  }

  getPersonDetail(id: string) {
    return this.http.get(this.getServiceUrl()+'/momApp/person/detail?id='+id).map(res => res.json()).catch(this.handleError);
  }
  updatePerson(person: person) {
    return this.http.post(this.getServiceUrl()+'/momApp/updatePerson', JSON.stringify(person)).map(res => res.json()).catch(this.handleError);
  }
  deletePerson(id: string) {
    return this.http.get(this.getServiceUrl()+'/momApp/deletePerson?id='+id).map(res => res.json()).catch(this.handleError);
  }
}
