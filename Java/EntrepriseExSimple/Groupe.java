import java.util.ArrayList;

public class Groupe {
    protected String nom;
    protected ArrayList<Contact> contacts;

    public Groupe(String nom){
        this.nom = nom;
        this.contacts = new ArrayList<Contact>();
    }

    public String getNom(){
        return nom;
    }

    public void setNom(String nouveauNom){
        this.nom = nouveauNom;
    }

    public void ajouterContact(Contact contact){
        if (this.contacts.contains(contact)){
            System.out.println("Ce contact est déjà dans ce groupe");
            return;
        }
        this.contacts.add(contact);
    }

    public void supprimerContact(Contact contact){
        if (!this.contacts.contains(contact)){
            System.out.println("Ce contact n'est pas dans ce groupe");
            return;
        }
        this.contacts.remove(contact);
    }

    public ArrayList<Contact> getContacts(){
        return contacts;
    }

    public String toString(){
        StringBuilder chaine = new StringBuilder("Nom du groupe: " + this.nom + "\n Contacts: \n");
        for (Contact contact : contacts) {
            chaine.append(contact.toString());
            chaine.append("\n");
        };
        return chaine.toString();
    }

}
