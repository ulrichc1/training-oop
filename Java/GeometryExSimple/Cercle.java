public class Cercle  extends FormeGeometrique implements Forme{
    private double rayon;

    public Cercle(double rayon, String nom, String couleur) {
        super(nom, couleur);
        this.rayon = rayon;
    }

    public double getRayon() {
        return this.rayon;
    }

    public void setRayon(double rayon) {
        this.rayon = rayon;
    }

    @Override
    public double calculerAire(){
        return Math.PI * (this.rayon * this.rayon);

    }
    @Override
    public double calculerPerimetre(){
        return 2 * Math.PI * this.rayon;
    }

    @Override
    public String getNom() {
        return "Cercle";
    }


}
