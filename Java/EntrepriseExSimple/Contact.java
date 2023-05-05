public class Contact {
    private String nom;
    private String adresse;
    private String telephone;
    private String email;

    public Contact (String nom, String adresse, String telephone, String email){
        this.nom = nom;
        this.adresse = adresse;
        this.telephone = telephone;
        this.email = email;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nouveauNom) {
        this.nom = nouveauNom;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String nouvelleAdresse) {
        this.adresse = nouvelleAdresse;
    }

    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String nouveauTelephone) {
        this.telephone = nouveauTelephone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String nouveauEmail) {
        this.email = nouveauEmail;
    }

    public String toString(){
        return "Nom: " + nom + "\nAdresse: " + adresse + "\nTelephone: " + telephone + "\nEmail: " + email;
    }


}






