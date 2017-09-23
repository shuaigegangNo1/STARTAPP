/**
 * Created by huangxuewen on 2017/9/20.
 */
import {Component} from "@angular/core";
import {AlertController, NavController, NavParams} from "ionic-angular";
import {PersonService} from "../../common/service/personService";
import {person} from "../../common/model/person"
import {PersonList} from "./personlist";
@Component({
  selector: 'app-person',
  templateUrl: 'person.html'
})
export class PersonComponent {
  person = new person();
  personId: string;
  showDelete = false;
  constructor(public navCtrl: NavController, public alertCtrl: AlertController,
              private personService: PersonService, private navParams: NavParams) {
    if (this.navParams.get('person')) {
      this.personId = this.navParams.get('person').id;
      this.getPersonDetail();
      this.showDelete = true;
    }
  }

  savePerson() {
    if (this.personId) {
      this.personService.updatePerson(this.person).subscribe(res => {
        console.log(">>>>data>>>", res);
        this.navCtrl.push(PersonList);
      });
    } else {
      this.person.create_date = '2017-09-26';
      this.personService.createPerson(this.person).subscribe(res => {
          console.log(">>>>data>>>", res);
          this.navCtrl.push(PersonList);
        }
      );
    }
  }

  getPersonDetail() {
    this.personService.getPersonDetail(this.personId).subscribe(res => {
      this.person = res.result;
    })
  }
  deletePerson() {
    this.personService.deletePerson(this.person.id).subscribe(res => {
        this.navCtrl.push(PersonList);
      }
    );
  }
}
