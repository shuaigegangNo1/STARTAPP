/**
 * Created by huangxuewen on 2017/9/20.
 */
import {Component} from "@angular/core";
import {AlertController, NavController} from "ionic-angular";
import {PersonService} from "../../common/service/personService";
import {person} from "../../common/model/person"
import {PersonList} from "./personlist";
@Component({
  selector: 'app-person',
  templateUrl: 'person.html'
})
export class PersonComponent{
  id: string;
  firstname: string;
  lastname: string;
  telephone: string;
  address: string;
  city: string;
  person =new person();
  constructor(public navCtrl: NavController, public alertCtrl: AlertController,
              private personService: PersonService){
  }
  addPerson() {
    this.person.id = this.id;
    this.person.firstname = this.firstname;
    this.person.lastname = this.lastname;
    this.person.telephone = this.telephone;
    this.person.city = this.city;
    this.person.address= this.address;
    this.person.create_date = '2017-09-26';
    this.personService.createPerson(this.person).subscribe(res => {
        console.log(">>>>data>>>",res);
        this.navCtrl.push(PersonList);
    }
    )
    // let NewPerson = {
    //   id: this.id,
    //
    // }
  }
}
