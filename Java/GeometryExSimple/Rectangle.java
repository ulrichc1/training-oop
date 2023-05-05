public class Rectangle  extends FormeGeometrique implements Forme{
    private double longueur;
    private double largeur;

    public Rectangle(double longueur, double largeur, String nom, String couleur){
        super(nom,couleur);
        this.longueur = longueur;
        this.largeur = largeur;
    }

    public double getLongueur(){
        return this.longueur;
    }
    public double getLargeur(){
        return this.largeur;
    }
    public void setLongueur(double longueur){
         this.longueur = longueur;
    }
    public void setLargeur(double largeur){
         this.largeur = largeur;
    }

    public double calculerAire(){
        return this.longueur * this.largeur;
    }

    public double calculerPerimetre(){
        return (this.longueur + this.largeur) * 2;
    }

}
