'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Linkedin } from 'lucide-react'

// Mock function to simulate contract interaction
const verifyMerkleProof = async (transactionHash: string, merkleProof: string): Promise<boolean> => {
  await new Promise(resolve => setTimeout(resolve, 1500))
  return transactionHash.startsWith('0x')
}

export function MerkleProofVerifierComponent() {
  const [transactionHash, setTransactionHash] = useState('')
  const [merkleProof, setMerkleProof] = useState('')
  const [verificationResult, setVerificationResult] = useState<boolean | null>(null)
  const [isVerifying, setIsVerifying] = useState(false)

  const handleVerify = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsVerifying(true)
    setVerificationResult(null)
    try {
      const result = await verifyMerkleProof(transactionHash, merkleProof)
      setVerificationResult(result)
    } catch (error) {
      console.error('Verification failed:', error)
      setVerificationResult(false)
    }
    setIsVerifying(false)
  }

  return (
    <div className="min-h-screen bg-black flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-md mb-8 flex items-center justify-between">
        <h2 className="text-white text-lg font-semibold">Made by 21BCE7553</h2>
        <a
          href="https://www.linkedin.com/in/vijay-tadepalli-279746226/"
          target="_blank"
          rel="noopener noreferrer"
          className="text-white hover:text-gray-300 transition-colors"
        >
          <Linkedin size={24} />
        </a>
      </div>
      <Card className="w-full max-w-md bg-gray-900 border-gray-800">
        <CardHeader>
          <CardTitle className="text-2xl font-bold text-center text-white">Merkle Proof Verifier</CardTitle>
          <CardDescription className="text-center text-gray-400">Verify blockchain transactions using Merkle proofs</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleVerify} className="space-y-6">
            <div className="space-y-2">
              <Label htmlFor="transactionHash" className="text-gray-300">Transaction Hash</Label>
              <Input
                id="transactionHash"
                value={transactionHash}
                onChange={(e) => setTransactionHash(e.target.value)}
                placeholder="0x..."
                required
                className="bg-gray-800 text-white border-gray-700 focus:border-gray-600 placeholder-gray-500"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="merkleProof" className="text-gray-300">Merkle Proof</Label>
              <Input
                id="merkleProof"
                value={merkleProof}
                onChange={(e) => setMerkleProof(e.target.value)}
                placeholder="Enter Merkle proof..."
                required
                className="bg-gray-800 text-white border-gray-700 focus:border-gray-600 placeholder-gray-500"
              />
            </div>
            <Button
              type="submit"
              disabled={isVerifying}
              className="w-full bg-white text-black hover:bg-gray-200 transition-colors"
            >
              {isVerifying ? 'Verifying...' : 'Verify'}
            </Button>
          </form>
        </CardContent>
        <CardFooter>
          <AnimatePresence mode="wait">
            {verificationResult !== null && (
              <motion.div
                key={verificationResult ? 'success' : 'failure'}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                transition={{ duration: 0.5, ease: "easeInOut" }}
                className="w-full text-center"
              >
                <motion.p
                  className={`text-lg font-semibold ${verificationResult ? 'text-green-400' : 'text-red-400'}`}
                  initial={{ scale: 0.9 }}
                  animate={{ scale: 1 }}
                  transition={{ type: "spring", stiffness: 200, damping: 10 }}
                >
                  {verificationResult
                    ? 'Transaction verified successfully!'
                    : 'Transaction verification failed.'}
                </motion.p>
              </motion.div>
            )}
          </AnimatePresence>
        </CardFooter>
      </Card>
    </div>
  )
}