public abstract class FormeGeometrique implements Forme {
    protected String nom;
    protected String couleur;

    public FormeGeometrique(String nom, String couleur) {
        this.nom = nom;
        this.couleur = couleur;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getCouleur() {
        return couleur;
    }

    public void setCouleur(String couleur) {
        this.couleur = couleur;
    }

    public String toString() {
        return "Nom: " + nom + ", Couleur: " + couleur;
    }
}