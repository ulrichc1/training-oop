import java.util.ArrayList;

public class Entreprise {
    protected String nom;
    protected ArrayList<Groupe> liste_groupes;

    public Entreprise(String nom){
        this.nom = nom;
        this.liste_groupes = new ArrayList<Groupe>();
    }

    public String getNom(){
        return nom;
    }

    public void setNom(String nouveauNom){
        this.nom = nouveauNom;
    }

    public void ajouterGroupe(Groupe groupe){
        if(this.liste_groupes.contains(groupe)){
            System.out.println("Ce groupe est déjà dans cette entreprise");
            return;
        }
        this.liste_groupes.add(groupe);
    }

    public void supprimerGroupe(Groupe groupe){
        if(!this.liste_groupes.contains(groupe)){
            System.out.println("Ce groupe n'est pas dans cette entreprise");
            return;
        }
        this.liste_groupes.remove(groupe);
    }

    public ArrayList<Groupe> getGroupes(){
        return liste_groupes;
    }

    public String toString(){
        StringBuilder chaine = new StringBuilder("Nom de l'entreprise: " + this.nom + "\n Groupes: \n");
        for (Groupe groupe : liste_groupes) {
            chaine.append(groupe.toString());
            chaine.append("\n");
        };
        return chaine.toString();
    }
}
